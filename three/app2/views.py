from django.shortcuts import render

# Create your views here.
def one(req):
    # return render(req, "one.html", {"name" : "Ankit Kumar"})

    student = {
        "names" : ["Ankit", "Rajesh", "Mohan"],
        "course" : ["Python", "Mysql", "Java"],
        "fees" : [10000, 20000, 30000]
    }

    return render(req, "one.html", {"stu" : student})


def two(req):
    coaname = "Samyak Classes"
    details = {
        "coa" : coaname,
        "name" : "Rohan Singh",
        "email" : "rohan@gmail.com",
        "course" : "Django",
        "fees" : 18000,
        "skills" : ["Html", "Css", "Javascript"]
    }
    return render(req, "two.html", {"data" : details})


def three(req):
    para = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellendus itaque recusandae cupiditate suscipit aperiam modi omnis vero quos labore quisquam, eos accusamus facilis? Enim non sunt amet molestiae at aliquid."
    name = "Rajesh Kumar"
    fees = 4000

    data = {'p' : para, 'n' : name, 'f' : fees}

    return render(req, "three.html", {'ok' : data})