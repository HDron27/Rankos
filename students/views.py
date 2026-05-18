import random
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from .models import Student, Group, Club, Profile
from .forms import StudentForm, RegisterForm, ProfileForm


def hello(request):
    return HttpResponse("""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Добро пожаловать — KontPortal</title>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;700;800;900&family=Space+Grotesk:wght@400;500&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box;}
body{font-family:'Space Grotesk',sans-serif;background:#06040f;color:#f1f0ff;min-height:100vh;display:flex;align-items:center;justify-content:center;overflow:hidden;}
canvas{position:fixed;inset:0;z-index:0;}
.content{position:relative;z-index:2;text-align:center;padding:2rem;max-width:700px;}
.logo-wrap{display:flex;align-items:center;justify-content:center;gap:.7rem;margin-bottom:3rem;}
.logo-icon{width:52px;height:52px;border-radius:14px;background:linear-gradient(135deg,#a855f7,#6366f1);display:flex;align-items:center;justify-content:center;box-shadow:0 0 30px rgba(168,85,247,.6);}
.logo-text{font-family:'Outfit',sans-serif;font-weight:800;font-size:1.5rem;letter-spacing:-.04em;}
.logo-text .k{color:#a855f7;}
h1{font-family:'Outfit',sans-serif;font-weight:900;font-size:clamp(2.5rem,7vw,4.5rem);letter-spacing:-.05em;line-height:1.05;margin-bottom:1.5rem;}
h1 .g{background:linear-gradient(90deg,#a855f7,#f472b6,#22d3ee);-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
p{color:rgba(241,240,255,.55);font-size:1.1rem;margin-bottom:2.5rem;line-height:1.7;font-weight:300;}
.btn{display:inline-flex;align-items:center;gap:.6rem;padding:.9rem 2.2rem;background:linear-gradient(135deg,#a855f7,#6366f1);color:white;text-decoration:none;border-radius:50px;font-weight:700;font-size:1rem;letter-spacing:.01em;box-shadow:0 4px 30px rgba(168,85,247,.45);transition:all .3s;}
.btn:hover{transform:translateY(-3px);box-shadow:0 12px 50px rgba(168,85,247,.65);}
.btn svg{transition:transform .25s;}
.btn:hover svg{transform:translateX(4px);}
.pill{display:inline-flex;align-items:center;gap:.5rem;padding:.35rem 1rem;border:1px solid rgba(168,85,247,.3);border-radius:20px;font-size:.78rem;color:rgba(241,240,255,.5);margin-bottom:2rem;background:rgba(168,85,247,.06);}
.pill span{width:6px;height:6px;border-radius:50%;background:#a855f7;box-shadow:0 0 8px #a855f7;}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-12px)}}
.float{animation:float 5s ease-in-out infinite;}
</style>
</head>
<body>
<canvas id="c"></canvas>
<div class="content">
    <div class="logo-wrap">
        <div class="logo-icon"><svg width="26" height="26" viewBox="0 0 20 20" fill="none"><path d="M3 14L7 6L10 12L13 8L17 14" stroke="white" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="10" cy="4" r="2" fill="rgba(255,255,255,.6)"/></svg></div>
        <div class="logo-text"><span class="k">K</span>ontPortal</div>
    </div>
    <div class="pill"><span></span>Платформа управления колледжем</div>
    <h1 class="float">Добро пожаловать на<br><span class="g">сайт колледжа!</span></h1>
    <p>Управляйте студентами, группами и кружками<br>в одном месте — быстро и удобно.</p>
    <a href="/students/" class="btn">Перейти к студентам <svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M5 12h14M13 6l6 6-6 6" stroke="white" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
</div>
<script>
const canvas=document.getElementById('c'),ctx=canvas.getContext('2d');
let W,H;function resize(){W=canvas.width=innerWidth;H=canvas.height=innerHeight;}resize();window.addEventListener('resize',resize);
const orbs=[
    {x:.1,y:.1,r:.45,c:'rgba(168,85,247,',ph:0,sp:.0002},
    {x:.9,y:.2,r:.35,c:'rgba(99,102,241,',ph:2,sp:.00025},
    {x:.5,y:.9,r:.45,c:'rgba(34,211,238,',ph:4,sp:.00018},
    {x:.85,y:.8,r:.25,c:'rgba(244,114,182,',ph:6,sp:.0003},
    {x:.15,y:.8,r:.2,c:'rgba(251,191,36,',ph:1,sp:.00035},
];
const stars=Array.from({length:80},()=>({x:Math.random()*innerWidth,y:Math.random()*innerHeight,r:Math.random()*1.5+.3,a:Math.random(),sp:Math.random()*.5+.2,ph:Math.random()*Math.PI*2}));
function draw(){
    ctx.clearRect(0,0,W,H);
    const t=Date.now();
    orbs.forEach(o=>{
        const cx=(o.x+Math.sin(t*o.sp+o.ph)*.1)*W;
        const cy=(o.y+Math.cos(t*o.sp+o.ph)*.08)*H;
        const r=o.r*Math.min(W,H);
        const g=ctx.createRadialGradient(cx,cy,0,cx,cy,r);
        g.addColorStop(0,o.c+'.22)');g.addColorStop(.5,o.c+'.08)');g.addColorStop(1,o.c+'0)');
        ctx.beginPath();ctx.fillStyle=g;ctx.arc(cx,cy,r,0,Math.PI*2);ctx.fill();
    });
    stars.forEach(s=>{
        const alpha=(.4+Math.sin(t*s.sp*.001+s.ph)*.4)*s.a;
        ctx.beginPath();ctx.arc(s.x,s.y,s.r,0,Math.PI*2);
        ctx.fillStyle=`rgba(255,255,255,${alpha})`;ctx.fill();
    });
    requestAnimationFrame(draw);
}
draw();
</script>
</body></html>""")


def get_or_create_profile(user):
    profile, _ = Profile.objects.get_or_create(user=user)
    return profile


@login_required
def student_list(request):
    students = Student.objects.select_related("group").prefetch_related("clubs").all()
    return render(request, "students/index.html", {"students": students})


@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, "students/detail.html", {"student": student})


@login_required
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm()
    return render(request, "students/add_student.html", {"form": form, "title": "Добавить студента"})


@login_required
def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm(instance=student)
    return render(request, "students/add_student.html", {"form": form, "title": "Редактировать студента", "edit": True})


@login_required
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect("student_list")
    return render(request, "students/confirm_delete.html", {"student": student})


@login_required
def group_list(request):
    groups = Group.objects.prefetch_related("students").all()
    return render(request, "students/groups.html", {"groups": groups})


@login_required
def club_list(request):
    clubs = Club.objects.prefetch_related("students").all()
    return render(request, "students/clubs.html", {"clubs": clubs})


@login_required
def profile_edit(request):
    profile = get_or_create_profile(request.user)
    if 'captcha_a' not in request.session:
        a, b = random.randint(1, 20), random.randint(1, 20)
        request.session['captcha_a'] = a
        request.session['captcha_b'] = b

    captcha_a = request.session['captcha_a']
    captcha_b = request.session['captcha_b']

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            answer = form.cleaned_data.get('captcha_answer')
            if answer != captcha_a + captcha_b:
                a, b = random.randint(1, 20), random.randint(1, 20)
                request.session['captcha_a'] = a
                request.session['captcha_b'] = b
                return JsonResponse({'success': False, 'error': 'captcha', 'message': 'Неверный ответ! Попробуйте снова.'})
            user = request.user
            new_username = form.cleaned_data.get('username')
            if new_username and new_username != user.username:
                if User.objects.filter(username=new_username).exclude(pk=user.pk).exists():
                    return JsonResponse({'success': False, 'error': 'username', 'message': 'Логин уже занят!'})
                user.username = new_username
            user.email = form.cleaned_data.get('email', '') or ''
            new_password = form.cleaned_data.get('new_password')
            if new_password:
                user.set_password(new_password)
            user.save()
            profile.display_name = form.cleaned_data.get('display_name', '')
            if 'avatar' in request.FILES:
                profile.avatar = request.FILES['avatar']
            profile.save()
            del request.session['captcha_a']
            del request.session['captcha_b']
            return JsonResponse({'success': True, 'message': 'Профиль обновлён!', 'username': user.username,
                                 'display_name': profile.display_name or user.username,
                                 'avatar_url': profile.get_avatar_url() or ''})
        else:
            errors = [e[0] for e in form.errors.values()]
            return JsonResponse({'success': False, 'error': 'form', 'message': ' '.join(errors)})
    return JsonResponse({'captcha_question': f"{captcha_a} + {captcha_b}"})


@login_required
def get_captcha(request):
    a, b = random.randint(1, 20), random.randint(1, 20)
    request.session['captcha_a'] = a
    request.session['captcha_b'] = b
    return JsonResponse({'question': f"{a} + {b} = ?"})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(username=form.cleaned_data["username"],
                                     email=form.cleaned_data["email"],
                                     password=form.cleaned_data["password"])
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "students/register.html", {"form": form})
