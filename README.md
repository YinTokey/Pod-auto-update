# pod_auto_script
A Python script that help you to auto update pod library.

# Useage
1. 


# 中文说明

### 这个脚本能做什么

在iOS领域使用pod来进行组件化开发的常常需要依赖一系列的操作，来实现Pod组件的更新目的。特别是一些业务关联性比较强的Pod组件，需要经常对其进行更新。随着组件的体积越来越大，每次更新的时候，需要在podspec文件里增加版本号，然后执行 pod lib lint，等待了好几分钟之后，好不容易podspec文件检查通过了，需要再进行打tag操作，然后再执行执行 pod repo push操作，然后再等好几分钟，才能将完成一个Pod组件的更新。整个流程不仅耗时，而且繁琐，机械化。这个脚本虽然没能提高pod lib lint 和pod repo push的执行速度，但是将这系列繁琐的操作，变成一句话完成。你可以一句话执行脚本，然后离开位置，去倒杯水，活动活动身子，稍微休息休息，再回来时，pod组件已经更新完毕并推送到远端了。


### 脚本所包含的操作：

1. podspec小版本自加一
2. pod lib lint语法检查，如果有依赖私有源，可以在顶部配置地址，既可用于github上的开源组件，也可用于gitlab内部团队的私有组件，至于bitbucket，没有试过，但是理论上应该是可行的，如果你发现不行，自己调试之后无法解决，可以联系我。
3. git add, git commit, git push，git tag , git push —tags 一系列git操作，完成提交与git的推送。
4. pod repo push操作，将pod组件推送到远端，完成一次pod组件的小版本更新

