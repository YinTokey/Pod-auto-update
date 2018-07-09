Pod::Spec.new do |s|
  s.name             = "UserModule"
  s.version          = "0.1.1"
  s.summary          = "UserModule summary"
  s.description      = "UserModule description"
  s.homepage         = "http://www.baidu.com"
  s.license          = "MIT"
  s.author           = "YinTokey"
  s.source           = { :git => "https://github.com/YinTokey/UserModule.git", :tag => s.version }
  s.platform     = :ios, "9.0"
  s.swift_version = "4.0"
  s.source_files = "UserModule-master/UserModule/*"
  s.dependency "Egen"
  s.dependency "Alamofire"
end