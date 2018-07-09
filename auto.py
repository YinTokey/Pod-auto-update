import os, sys
import fileinput

# ======================  edit by yourself  ======================
sources = [
          #'https://github.com/YinTokey/Egen.git',
          ]

project_name = 'UserModule-master'
podspec_file_name = 'UserModule.podspec'


# ==================================================================




new_tag = ""
lib_command = ""
pod_push_command = ""
spec_file_path = "./" + podspec_file_name
find_version_flag = False




def podCommandEdit():
    global lib_command
    global pod_push_command
    source_suffix = 'https://github.com/CocoaPods/Specs.git --allow-warnings'
    lib_command = 'pod lib lint --sources='
    pod_push_command = 'pod repo push ' + project_name + ' ' + podspec_file_name
    if len(sources) > 0:
        # rely on  private sourece
        pod_push_command += ' --sources='

        for index,source in enumerate(sources):
            lib_command += source
            lib_command += ','
            pod_push_command += source
            pod_push_command += ','

        lib_command += source_suffix
        pod_push_command += source_suffix

    else:
        lib_command = 'pod lib lint'


def updateVersion():
    f = open(spec_file_path,'r+')
    infos = f.readlines()
    f.seek(0,0)
    file_data = ""
    global find_version_flag

    for line in infos:
        if line.find(".version") != -1:
            if find_version_flag == False:
                # find s.version = "xxxx"
                length = len(line)
                substr = line[length-4:length-2]
                global new_tag
                if substr.find(".") != -1:
                    substr = line[length-3:length-2]

                num = int(substr) + 1
                newsubstr = str(num)
                line = line.replace(substr, newsubstr)
                new_tag = line[length-8:length-2]



                find_version_flag = True

        file_data += line
    
    with open(spec_file_path,'w',) as f1:
        f1.write(file_data)
    
    f.close()

    print "--------- auto update version -------- "


def libLint():
    print("-------- waiting for pod lib lint checking ...... ---------")
    os.system(lib_command)

def gitOperation():
    os.system('git add .')
    commit_desc = "version_" + new_tag
    commit_command = 'git commit -m "' + commit_desc + '"'
    os.system(commit_command)
    # git push
    r = os.popen('git symbolic-ref --short -q HEAD')
    current_branch = r.read()
    r.close()
    push_command = 'git push origin ' + current_branch
    
    # tag
    tag_command = 'git tag -m "' + new_tag + '" ' + new_tag
    os.system(tag_command)
    
    # push tags
    os.system('git push --tags')

def podPush():
    print("--------  waiting for pod push  ...... ---------")
    os.system(pod_push_command)



# run commands


updateVersion()
podCommandEdit()
libLint()
gitOperation()
podPush()


