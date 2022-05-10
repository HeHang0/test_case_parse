# -*- coding: UTF-8 -*-
try:
    from uitrace.api import *
except:
    print("cannot import module uitrace.api")

class TestVideoCollection:
    @classmethod
    def setup_class(cls):
        init_driver()
        press(DeviceButton.HOME)
        time.sleep(1)


    @classmethod
    def teardown_class(cls):
        press(DeviceButton.HOME)
        stop_driver()

    def setup_method(self,method):
        start_app("com.oohoo.videocollection")
        click('//android.widget.RelativeLayout[2]/android.widget.TextView[@text="进入" and @resource-id="com.oohoo.videocollection:id/welcome_btn"]', by=DriverType.UI, timeout=20)
        time.sleep(2)

    def teardown_method(self,method):
        stop_app("com.oohoo.videocollection")
        press(DeviceButton.HOME)
        time.sleep(1)
    
    def test_douban(self):
        click('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageButton', by=DriverType.UI, timeout=20)
        time.sleep(2)
        click('//android.widget.CheckedTextView[@text="豆瓣Top250" and @resource-id="com.oohoo.videocollection:id/design_menu_item_text"]', by=DriverType.UI, timeout=10)
        click('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[1]', by=DriverType.UI, timeout=10)
        time.sleep(3)

    
    @pytest.mark.run(order=1)
    def test_live(self):
        click('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageButton', by=DriverType.UI, timeout=20)
        time.sleep(2)
        click('//android.widget.CheckedTextView[@text="直播" and @resource-id="com.oohoo.videocollection:id/design_menu_item_text"]', by=DriverType.UI, timeout=20)
        click('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[1]', by=DriverType.UI, timeout=20)
        time.sleep(3)

    def test_cloudmusic(self):
        click('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageButton', by=DriverType.UI, timeout=20)
        time.sleep(2)
        click('//android.widget.CheckedTextView[@text="云音乐" and @resource-id="com.oohoo.videocollection:id/design_menu_item_text"]', by=DriverType.UI, timeout=20)
        click('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[1]', by=DriverType.UI, timeout=20)
        time.sleep(10)
