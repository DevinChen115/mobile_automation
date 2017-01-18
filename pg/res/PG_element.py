import os

pkg = os.getenv('PGPKG')
# Package 相關
Package={}
Package['appPackage'] = pkg
Package['appActivity'] = pkg+'.MainPage'

# 第一次開啟的登入頁
LoginPage = {}
LoginPage['skip'] = pkg+':id/login_skip_btn'
LoginPage['topImage'] = pkg+':id/top_images'
LoginPage['more'] = pkg+':id/more_login_option_btn'
LoginPage['FB'] = pkg+':id/explore_login_btn_fb'
LoginPage['IG'] = pkg+':id/explore_login_btn_ig'
LoginPage['G'] = pkg+':id/explore_login_btn_g'
LoginPage['Mail'] = pkg+':id/sign_up_email'
