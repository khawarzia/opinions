from django.shortcuts import render,redirect
from .models import debate as post
from django.contrib.auth.decorators import login_required

def base(request):
    template = 'base.html'
    context = {}
    return render(request,template,context)

@login_required(login_url = '/login')
def profile(request):
    template = 'profile.html'
    context = {}
    posts = []
    allposts = post.objects.all()
    for i in allposts:
        if request.user == i.user:
            posts.append(i)
    context['posts'] = posts
    return render(request,template,context)

@login_required(login_url = '/login')
def newpost(request,sel):
    template = 'new-post.html'
    if (int(sel) > 7 and int(sel) < 0):
        sel = '7'
    context = {'sel':sel}
    if request.method == 'POST':
        count = 0
        a = request.POST
        obj = post()
        obj.user = request.user
        obj.title = a['title']
        if (sel == '1'):
            obj.argtype = 'Argument from Analogy'
            obj.argtypenum = 1
        elif (sel == '2'):
            obj.argtype = 'Argument from Correlation to Cause'
            obj.argtypenum = 2
        elif (sel == '3'):
            obj.argtype = 'Argument from positive/negative Consequences'
            obj.argtypenum = 3
        elif (sel == '4'):
            obj.argtype = 'Argument from the Position to know'
            obj.argtypenum = 4
        elif (sel == '5'):
            obj.argtype = 'Appeal to Expert Opinion'
            obj.argtypenum = 5
        elif (sel == '6'):
            obj.argtype = 'Appeal to Popular Opinion'
            obj.argtypenum = 6
        else:
            obj.argtype = 'Action Scheme'
        try:
            obj.a1 = (a['situation'])
            count = count + 1
            try:
                obj.a2 = (a['sitcon1'])
                count = count + 1
                try:
                    obj.a3 = (a['sitcon11'])
                    count = count + 1
                    try:
                        obj.a4 = (a['sitcon111'])
                        count = count + 1
                        try:
                            obj.a5 = (a['sitcon1111'])
                            count = count + 1
                            try:
                                obj.a6 = (a['sitcon11111'])
                                count = count + 1
                                try:
                                    obj.a7 = (a['sitcon111111'])
                                    count = count + 1
                                except:
                                    pass
                            except:
                                pass
                        except:
                            pass
                    except:
                        pass
                except:
                    pass
            except:
                pass
        except:
            pass
        obj.anum = count
        count = 0
        try:
            obj.b1 = (a['action'])
            count = count + 1
            try:
                obj.b2 = (a['actcon1'])
                count = count + 1
                try:
                    obj.b3 = (a['actcon11'])
                    count = count + 1
                    try:
                        obj.b4 = (a['actcon111'])
                        count = count + 1
                        try:
                            obj.b5 = (a['actcon1111'])
                            count = count + 1
                            try:
                                obj.b6 = (a['actcon11111'])
                                count = count + 1
                                try:
                                    obj.b7 = (a['actcon111111'])
                                    count = count + 1
                                except:
                                    pass
                            except:
                                pass
                        except:
                            pass
                    except:
                        pass
                except:
                    pass
            except:
                pass
        except:
            pass
        obj.bnum = count
        count = 0
        try:
            obj.c1 = (a['goal'])
            count = count + 1
            try:
                obj.c2 = (a['goalcon1'])
                count = count + 1
                try:
                    obj.c3 = (a['goalcon11'])
                    count = count + 1
                    try:
                        obj.c4 = (a['goalcon111'])
                        count = count + 1
                        try:
                            obj.c5 = (a['goalcon1111'])
                            count = count + 1
                            try:
                                obj.c6 = (a['goalcon11111'])
                                count = count + 1
                                try:
                                    obj.c7 = (a['goalcon111111'])
                                    count = count + 1
                                except:
                                    pass
                            except:
                                pass
                        except:
                            pass
                    except:
                        pass
                except:
                    pass
            except:
                pass
        except:
            pass
        obj.cnum = count
        count = 0
        try:
            obj.d1 = (a['provalue'])
            count = count + 1
            try:
                obj.d2 = (a['procon1'])
                count = count + 1
                try:
                    obj.d3 = (a['procon11'])
                    count = count + 1
                    try:
                        obj.d4 = (a['procon111'])
                        count = count + 1
                        try:
                            obj.d5 = (a['procon1111'])
                            count = count + 1
                            try:
                                obj.d6 = (a['procon11111'])
                                count = count + 1
                                try:
                                    obj.d7 = (a['procon111111'])
                                    count = count + 1
                                except:
                                    pass
                            except:
                                pass
                        except:
                            pass
                    except:
                        pass
                except:
                    pass
            except:
                pass
        except:
            pass
        obj.dnum = count
        count = 0
        obj.save()
        return redirect('/profile')
    return render(request,template,context)

@login_required(login_url = '/login')
def viewpost(request,id):
    obj = post.objects.get(pk=id)
    template = 'view-post.html'
    context = {'post':obj}
    return render(request,template,context)

@login_required(login_url = '/login')
def counterpost(request,id,sel):
    template = 'new-post.html'
    if (int(sel) > 7 and int(sel) < 0):
        sel = '7'
    context = {'sel':sel}
    if request.method == 'POST':
        count = 0
        a = request.POST
        obj = post()
        obj.user = request.user
        obj.title = a['title']
        if (sel == '1'):
            obj.argtype = 'Argument from Analogy'
            obj.argtypenum = 1
        elif (sel == '2'):
            obj.argtype = 'Argument from Correlation to Cause'
            obj.argtypenum = 2
        elif (sel == '3'):
            obj.argtype = 'Argument from positive/negative Consequences'
            obj.argtypenum = 3
        elif (sel == '4'):
            obj.argtype = 'Argument from the Position to know'
            obj.argtypenum = 4
        elif (sel == '5'):
            obj.argtype = 'Appeal to Expert Opinion'
            obj.argtypenum = 5
        elif (sel == '6'):
            obj.argtype = 'Appeal to Popular Opinion'
            obj.argtypenum = 6
        else:
            obj.argtype = 'Action Scheme'
        try:
            obj.a1 = (a['situation'])
            count = count + 1
            try:
                obj.a2 = (a['sitcon1'])
                count = count + 1
                try:
                    obj.a3 = (a['sitcon11'])
                    count = count + 1
                    try:
                        obj.a4 = (a['sitcon111'])
                        count = count + 1
                        try:
                            obj.a5 = (a['sitcon1111'])
                            count = count + 1
                            try:
                                obj.a6 = (a['sitcon11111'])
                                count = count + 1
                                try:
                                    obj.a7 = (a['sitcon111111'])
                                    count = count + 1
                                except:
                                    pass
                            except:
                                pass
                        except:
                            pass
                    except:
                        pass
                except:
                    pass
            except:
                pass
        except:
            pass
        obj.anum = count
        count = 0
        try:
            obj.b1 = (a['action'])
            count = count + 1
            try:
                obj.b2 = (a['actcon1'])
                count = count + 1
                try:
                    obj.b3 = (a['actcon11'])
                    count = count + 1
                    try:
                        obj.b4 = (a['actcon111'])
                        count = count + 1
                        try:
                            obj.b5 = (a['actcon1111'])
                            count = count + 1
                            try:
                                obj.b6 = (a['actcon11111'])
                                count = count + 1
                                try:
                                    obj.b7 = (a['actcon111111'])
                                    count = count + 1
                                except:
                                    pass
                            except:
                                pass
                        except:
                            pass
                    except:
                        pass
                except:
                    pass
            except:
                pass
        except:
            pass
        obj.bnum = count
        count = 0
        try:
            obj.c1 = (a['goal'])
            count = count + 1
            try:
                obj.c2 = (a['goalcon1'])
                count = count + 1
                try:
                    obj.c3 = (a['goalcon11'])
                    count = count + 1
                    try:
                        obj.c4 = (a['goalcon111'])
                        count = count + 1
                        try:
                            obj.c5 = (a['goalcon1111'])
                            count = count + 1
                            try:
                                obj.c6 = (a['goalcon11111'])
                                count = count + 1
                                try:
                                    obj.c7 = (a['goalcon111111'])
                                    count = count + 1
                                except:
                                    pass
                            except:
                                pass
                        except:
                            pass
                    except:
                        pass
                except:
                    pass
            except:
                pass
        except:
            pass
        obj.cnum = count
        count = 0
        try:
            obj.d1 = (a['provalue'])
            count = count + 1
            try:
                obj.d2 = (a['procon1'])
                count = count + 1
                try:
                    obj.d3 = (a['procon11'])
                    count = count + 1
                    try:
                        obj.d4 = (a['procon111'])
                        count = count + 1
                        try:
                            obj.d5 = (a['procon1111'])
                            count = count + 1
                            try:
                                obj.d6 = (a['procon11111'])
                                count = count + 1
                                try:
                                    obj.d7 = (a['procon111111'])
                                    count = count + 1
                                except:
                                    pass
                            except:
                                pass
                        except:
                            pass
                    except:
                        pass
                except:
                    pass
            except:
                pass
        except:
            pass
        obj.dnum = count
        count = 0
        obj.save()
        obj2 = post.objects.get(pk=id)
        obj2.link.add(obj)
        obj2.linkcheck = True
        obj2.save()
        return redirect('/view-post/'+str(id))
    return render(request,template,context)

@login_required(login_url = '/login')
def agree(request,id,t):
    obj = post.objects.get(pk=id)
    if (t == 'a1'):
        obj.al1 = obj.al1 + 1
    if (t == 'a2'):
        obj.al2 = obj.al2 + 1
    if (t == 'a3'):
        obj.al3 = obj.al3 + 1
    if (t == 'a4'):
        obj.al4 = obj.al4 + 1
    if (t == 'a5'):
        obj.al5 = obj.al5 + 1
    if (t == 'a6'):
        obj.al6 = obj.al6 + 1
    if (t == 'a7'):
        obj.al7 = obj.al7 + 1
    if (t == 'b1'):
        obj.bl1 = obj.bl1 + 1
    if (t == 'b2'):
        obj.bl2 = obj.bl2 + 1
    if (t == 'b3'):
        obj.bl3 = obj.bl3 + 1
    if (t == 'b4'):
        obj.bl4 = obj.bl4 + 1
    if (t == 'b5'):
        obj.bl5 = obj.bl5 + 1
    if (t == 'b6'):
        obj.bl6 = obj.bl6 + 1
    if (t == 'b7'):
        obj.bl7 = obj.bl7 + 1
    if (t == 'c1'):
        obj.cl1 = obj.cl1 + 1
    if (t == 'c2'):
        obj.cl2 = obj.cl2 + 1
    if (t == 'c3'):
        obj.cl3 = obj.cl3 + 1
    if (t == 'c4'):
        obj.cl4 = obj.cl4 + 1
    if (t == 'c5'):
        obj.cl5 = obj.cl5 + 1
    if (t == 'c6'):
        obj.cl6 = obj.cl6 + 1
    if (t == 'c7'):
        obj.cl7 = obj.cl7 + 1
    if (t == 'd1'):
        obj.dl1 = obj.dl1 + 1
    if (t == 'd2'):
        obj.dl2 = obj.dl2 + 1
    if (t == 'd3'):
        obj.dl3 = obj.dl3 + 1
    if (t == 'd4'):
        obj.dl4 = obj.dl4 + 1
    if (t == 'd5'):
        obj.dl5 = obj.dl5 + 1
    if (t == 'd6'):
        obj.dl6 = obj.dl6 + 1
    if (t == 'd7'):
        obj.dl7 = obj.dl7 + 1
    obj.save()
    return redirect('/view-post/'+str(id))

@login_required(login_url = '/login')
def disagree(request,id,t):
    obj = post.objects.get(pk=id)
    if (t == 'a1'):
        obj.ad1 = obj.ad1 + 1
    if (t == 'a2'):
        obj.ad2 = obj.ad2 + 1
    if (t == 'a3'):
        obj.ad3 = obj.ad3 + 1
    if (t == 'a4'):
        obj.ad4 = obj.ad4 + 1
    if (t == 'a5'):
        obj.ad5 = obj.ad5 + 1
    if (t == 'a6'):
        obj.ad6 = obj.ad6 + 1
    if (t == 'a7'):
        obj.ad7 = obj.ad7 + 1
    if (t == 'b1'):
        obj.bd1 = obj.bd1 + 1
    if (t == 'b2'):
        obj.bd2 = obj.bd2 + 1
    if (t == 'b3'):
        obj.bd3 = obj.bd3 + 1
    if (t == 'b4'):
        obj.bd4 = obj.bd4 + 1
    if (t == 'b5'):
        obj.bd5 = obj.bd5 + 1
    if (t == 'b6'):
        obj.bd6 = obj.bd6 + 1
    if (t == 'b7'):
        obj.bd7 = obj.bd7 + 1
    if (t == 'c1'):
        obj.cd1 = obj.cd1 + 1
    if (t == 'c2'):
        obj.cd2 = obj.cd2 + 1
    if (t == 'c3'):
        obj.cd3 = obj.cd3 + 1
    if (t == 'c4'):
        obj.cd4 = obj.cd4 + 1
    if (t == 'c5'):
        obj.cd5 = obj.cd5 + 1
    if (t == 'c6'):
        obj.cd6 = obj.cd6 + 1
    if (t == 'c7'):
        obj.cd7 = obj.cd7 + 1
    if (t == 'd1'):
        obj.dd1 = obj.dd1 + 1
    if (t == 'd2'):
        obj.dd2 = obj.dd2 + 1
    if (t == 'd3'):
        obj.dd3 = obj.dd3 + 1
    if (t == 'd4'):
        obj.dd4 = obj.dd4 + 1
    if (t == 'd5'):
        obj.dd5 = obj.dd5 + 1
    if (t == 'd6'):
        obj.dd6 = obj.dd6 + 1
    if (t == 'd7'):
        obj.dd7 = obj.dd7 + 1
    obj.save()
    return redirect('/view-post/'+str(id))