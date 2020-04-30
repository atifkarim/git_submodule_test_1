This repository I am using to learn about **git submodule**
---
Here, I am assuming my parent [work dir](https://github.com/atifkarim/git_submodule_test_1) is **git_submodule_test_1** and [submodule work repo](https://github.com/atifkarim/git_submodule_test_2) is **git_submodule_test_2**

Some useful link I have found regarding **git submodule** are
---
[git official docs](https://git-scm.com/book/en/v2/Git-Tools-Submodules) <br />
[personal blog](https://github.blog/2016-02-01-working-with-submodules/)

<h4>To add a module using git submodule you can use the following command </h4>

```
git submodule add https://github.com/atifkarim/git_submodule_test_2
```

**Then, use in the main.py the following lines to run the main code** <br />
```from git_submodule_test_2.img_process import *```

**Another way of adding submodule** <br />

```git submodule add https://github.com/atifkarim/git_submodule_test_2 git_submodule_test_2```


**If you want to delete the submodule and faced any problem like 'git_submodule_test_2' already exists in the index then follow** [personal blog 1](https://stackoverflow.com/questions/12898278/issue-with-adding-common-code-as-git-submodule-already-exists-in-the-index) 

**Here , I have written the steps:** <br />
**issue:** Deleted submodule folder but then want to add again but showing error >>  ```'git_submodule_test_2' already exists in the index``` <br />
**Then I have done:** <br /> 
```git ls-files --stage git_submodule_test_2``` *to check submodule* <br />
```git rm --cached git_submodule_test_2``` *to remove submodule* <br />
```git submodule add https://github.com/atifkarim/git_submodule_test_2 git_submodule_test_2``` *to add submodule* <br />

**But yes, there is some problem might be ocurred like while you want to add it can show error because your delete process was not OK. So use--**

```
git submodule add --force https://github.com/atifkarim/git_submodule_test_2 git_submodule_test_2
```
*used --force tag* <br />

**The problem occurs MAYBE there is a .gitmodules file which is hidden. YOU have to delete this also. If you delete it then without using --force tag you can again add submodule**

**To add, commit, push any repo where you have just added a submodule but NO change in the SUBMODULE then do**
```
git submodule update --init --recursive
git add .
git commit -m "commit message"
git push origin master

```

**To clone a repository which has git submodule then do the following**
For example here parent repo is: https://github.com/atifkarim/git_submodule_test_1, so, do <br />
```
git clone https://github.com/atifkarim/git_submodule_test_1.git
```
But you will see that submodule folder **git_submodule_test_2** is empty. So do the following <br/>
```
git submodule init
git submodule update
```

**To overcome all of this hassle with a single command use**
```
git clone --recurse-submodules https://github.com/atifkarim/git_submodule_test_1
``` 
*it is the url of the parent repo*

**If any change is done in the submodule by you then how to add, commit, push from parent repo ??**
<br/>[look here](https://stackoverflow.com/questions/5542910/how-do-i-commit-changes-in-a-git-submodule)

<br/>**It is a little bit problematic thing I guess**

**If a change in the submodule by it's owner is happened and you want to track then do**
```
git submodule update --remote git_submodule_test_2

```
And then again add, commit, push it
