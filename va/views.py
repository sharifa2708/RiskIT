from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import InputForm


def index(request):
    print([q.id for q in Ques.objects.all()])
    return render(request, 'va/index.html')

def question(request,ques_id):
    all_ques = Ques.objects.all()
    q = Ques.objects.get(id=ques_id)
    # print([q.id for q in all_ques])
    if request.method == 'POST':
        print(request.POST)
        # form = InputForm(request.POST)
        # print("\n\npokayyyy\n\n")

        new_bunch = None
        if 'answerbunch' in request.session:
            new_bunch = AnsBunch.objects.get(id=request.session['answerbunch'])
        else:
            new_bunch = AnsBunch()
            new_bunch.save()
            request.session['answerbunch'] = new_bunch.id

        new_ans = Ans(ques=q, bunch=new_bunch)
        new_ans.save()

        for x in request.POST:
            if x.__contains__('choice'):
                print("saving...")
                p_id = int(x.replace('choice', ''))
                p_q = Subpart.objects.get(id=p_id)

                p_ans = SubpartAns(
                    subpart = p_q,
                    score = int(request.POST[x]),
                    ans = new_ans,
                )
                p_ans.save()
                print("saved...")

        q_no = q.ques_num
        # Try to get next question
        try:
            next_q = Ques.objects.get(ques_num=q_no+1)
            return redirect('ques', ques_id=next_q.id)
        except:
            del request.session['answerbunch']
            request.session['success_page_answer_bunch_id'] = new_bunch.id
            return redirect('success_page')


        if False:
            ans = request.POST['choice']

            new_ans = Ans(ques=q, score=int(ans))

            bunch = None
            if 'answerbunch' in request.session:
                bunch = AnsBunch.objects.get(id=request.session['answerbunch'])
            else:
                bunch = AnsBunch()
                bunch.save()
                request.session['answerbunch'] = bunch.id
            # bunch.add(new_ans)
            new_ans.bunch = bunch
            new_ans.save()

            q_no = q.ques_num
            # Try to get next question
            try:
                next_q = Ques.objects.get(ques_num=q_no+1)
                return redirect('ques', ques_id=next_q.id)
            # No next question? You're done
            except:
                del request.session['answerbunch']
                return redirect('index')

            # for c in all_ques:
            #     if c.ques_num == ques_id:
            #         c.score_for_subpart=ans
            # ques=Ques()
            # ques.score_for_subpart = ans
            # ques.save()

        # if request.POST.get('score'):
        #     ques = Ques()
        #     ques.score = request.POST.get('score')
        #     ques.save()
    else:
        form = InputForm()
    context = {'all_ques': all_ques, 'q': Ques.objects.get(id=ques_id),
               'form': form,
               }

    return render(request, 'va/ques.html',context)


def success_page(request):
    if not 'success_page_answer_bunch_id' in request.session:
        return redirect('index')
    new_bunch = AnsBunch.objects.get(id=request.session['success_page_answer_bunch_id'])
    del request.session['success_page_answer_bunch_id']
    return render(
        request,
        'va/success.html',
        {'ansbunch': new_bunch}
    )


def add_score(request):
    if request.method == 'POST':
        if request.POST.get('score'):
            ques = Ques()
            ques.score = request.POST.get('score')
            ques.save()

            return render(request, 'va/ques.html')

    else:
        return render(request, 'va/ques.html')
