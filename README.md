

### Why develop this script
When we develop some Pod components in iOS field, we have to type so many git and pod commands on the terminal. If the Pod project is very large, and it will cost a lot of time to run the `pod lib lint` and `pod repo push`, you also have to update the pod version in `.podspec` file and push tags. It's a very boring and mechanized process. This script will free you from this process.

### What actions this script contained
**1.** Making the small version plus one in the `.podspec` file, such as change the `s.version = "0.1.1"` to `s.version = "0.1.2"`, or `s.version = "1.2.15"` to `s.version = "1.2.16"`, or `s.version = "10.22.0.15"` to `s.version = "10.22.0.16"`, no mater what your version looks like, it will update the last digit of the version number.


**2.** Run the `pod lib lint`. If your Pod project dependent on other private sources, you can configure it on the top of the script. It's work well on Github and GitLab. As for BitBucket, you can try it. If you find it can't work, let me konw.

**3.** Run a series of git operations, such as git add, git commit, git push, git tag, git push --tags.

**4.** Run the `pod repo push`

### Useage

**1.** Add the `auto.py` to your pod project and make sure it is in the same directory as the `.podspec` file.

![](https://github.com/YinTokey/Blog_Posts/raw/master/pod_auto_script/1.png?raw=true)

You can add this python script file to `.gitignore` If you think it is necessary.

**2.** Open the `auto.py` file, and configure it on the top. Such like this screenshot
![](https://github.com/YinTokey/Blog_Posts/raw/master/pod_auto_script/2.png?raw=true)

You can add the dependent sources in the `sources` array, but you don't need the add the `https://github.com/CocoaPods/Specs.git`.

**3.** Open the terminal, navigate to the directory where `poedspec` and this script file are located.

**4.** Run the `python auto.py` command on the terminal. It's will auto update your Pod project version and auto push it to origin. If failed, you have to check and make sure your `podspec` configuration is correct.


# 中文说明

### 使用场景

在 iOS 领域使用 Pod 来进行组件化开发时常常需要手动进行一系列的操作，来实现Pod 组件的更新目的。特别是一些业务关联性比较强的 Pod 组件，需要经常对其进行更新。随着组件的体积越来越大，每次更新的时候，执行 pod lib lint，等待了好几分钟之后，好不容易 podspec 文件检查通过了，需要再进行打 tag 操作，然后再执行 pod repo push 操作，然后再等好几分钟，才能将完成一个 Pod 组件的更新。整个流程不仅耗时，而且繁琐，机械化。这个脚本虽然没能提高pod lib lint 和 pod repo push 的执行速度，但是将这系列繁琐的操作，变成一句话完成。你可以一句话执行脚本，然后离开位置，去倒杯水，活动活动身子，稍微休息休息，再回来时，Pod 组件已经更新完毕并推送到远端了。

### 前提条件：

你的 Pod 组件必须是已经正确配置，且之前有过手动输命令行更新的经历。

### 脚本所包含的操作：
**1.** podspec 小版本自加一，比如
`s.version = "0.1.1"` 自动变成 `s.version = "0.1.2"`，或者`s.version = "10.22.0.15"` 变成`s.version = "10.22.0.16"`，无论版本长什么样，只要写法是能通过 podspec 的语法检查，那么它就可以自动更新最后一位。

**2.** pod lib lint 语法检查，如果有依赖私有源，可以在顶部配置地址，既可用于github 上的开源组件，也可用于 Gitlab 内部团队的私有组件，至于Bitbucket，没有试过，但是理论上应该是可行的，如果你发现不行，自己调试之后无法解决，可以在 issue 上提出。

**3.** git add, git commit, git push，git tag , git push —tags 一系列git 操作，完成提交与 Tag 的推送。

**4.** pod repo push 操作，将pod组件推送到远端，完成一次pod组件的小版本更新。

### 怎么使用

**1.** 将`auto.py`文件拖入Pod组件工程中，并保证它与 podspec 文件处于同一级别的目录，如下图
![](https://github.com/YinTokey/Blog_Posts/blob/master/pod_auto_script/1.png?raw=true)

如果你觉得有必要，可自行将`auto.py`加入到 .gitignore 中。

**2.** 打开`auto.py`在顶部虚线框中进行配置。如下图

![](https://github.com/YinTokey/Blog_Posts/blob/master/pod_auto_script/2.png?raw=true)

第一项 sources 是pod组件所依赖的私有源地址，它是一个数组，可以填写多个私有源，用逗号隔开。其中 https://github.com/CocoaPods/Specs.git 不需要填写，脚本内已经写了。

第二项是你的项目名称

第三项是podspec文件名

**3.** 打开终端，cd 到这个脚本文件所在目录中，执行 `python auto.py`，即可开始小版本自动升级。如果你的 Pod 已经配置正确，并且之前有过手动输入指令进行升级的经历，那么脚本应该是能成功运行的。

