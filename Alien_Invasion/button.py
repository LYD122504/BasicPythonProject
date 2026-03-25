import pygame.font
# pygame.font的作用是让pygame能够将文本渲染到屏幕上
class Button():
    def __init__(self,setting,screen,msg):
        '''初始化按钮属性'''
        # 其中的msg是要在按钮中显示的文本
        self.screen=screen
        self.screen_rect=screen.get_rect()
        # 设置按钮的尺寸和其他属性
        self.width,self.height=200,50
        # 设置按钮颜色为亮绿色
        self.button_color=(0,255,0)
        # 设置按钮文本颜色为白色
        self.text_color=(255,255,255)
        # 设置渲染文本的字体,None表示采用默认字体,48则是字体字号
        self.font=pygame.font.SysFont(None,48)
        # 创建按钮的rect对象,并使其居中
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center
        # 按钮的标签只需要创建一次
        # Pygame会将想要显示的字符串渲染为图像来处理文本
        self.pre_msg(msg)
    
    def pre_msg(self,msg):
        '''将msg渲染为图像,并使其在按钮上居中'''
        # font render将存储在msg文本转换为图像,这个图像会存储在msg_image
        # 第二个布尔参数,用来控制指定开启或者关闭反锯齿功能.
        self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center

    def draw_button(self):
        '''绘制一个用颜色填充的按钮,再绘制文本'''
        # fill用来绘制表示按钮的矩形
        # blit向其中传递一幅图像以及与这个图像相关联的rect对象 
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)