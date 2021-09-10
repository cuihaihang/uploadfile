# -*- coding: utf-8 -*-
# coding=utf-8
import os
import shutil
import zipfile

from flask import Flask, render_template, send_from_directory, make_response
from flask_bootstrap import Bootstrap
from wtforms import FileField, StringField, SubmitField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed


class UploadForm(FlaskForm):
    name = StringField(u'姓名', validators=[InputRequired()])
    numID = StringField(u'学号', validators=[InputRequired()])
    xingchengma = FileField(u'行程码', validators=[FileRequired(),  # FileRequired必须上传
                                                FileAllowed(['jpg', 'png', 'jpeg'])  # FileAllowed:必须为指定的格式的文件
                                                ])
    jiankangma = FileField(u'健康码', validators=[FileRequired(),  # FileRequired必须上传
                                               FileAllowed(['jpg', 'png', 'jpeg'])  # FileAllowed:必须为指定的格式的文件
                                               ])
    hesuanjiance = FileField(u'核酸检测报告', validators=[FileRequired(),  # FileRequired必须上传
                                                    FileAllowed(['jpg', 'png', 'jpeg'])  # FileAllowed:必须为指定的格式的文件
                                                    ])
    yimiaojiezhong = FileField(u'疫苗接种凭证', validators=[FileRequired(),  # FileRequired必须上传
                                                      FileAllowed(['jpg', 'png', 'jpeg'])  # FileAllowed:必须为指定的格式的文件
                                                      ])
    jiaotonggongju = FileField(u'乘坐交通工具始发及经停站点信息', validators=[FileRequired(),  # FileRequired必须上传
                                                               FileAllowed(['jpg', 'png', 'jpeg'])
                                                               # FileAllowed:必须为指定的格式的文件
                                                               ])
    submit = SubmitField(u'添加')


bootstrap = Bootstrap()
app = Flask(__name__)
app.secret_key = '2021521494'
bootstrap.init_app(app)
UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'recfiles')


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    form = UploadForm()
    if form.validate_on_submit():
        name = form.name.data
        numID = form.numID.data
        xingchengma = form.xingchengma.data
        nxingchengma = xingchengma.filename.split('.')[-1]
        jiankangma = form.jiankangma.data
        njiankangma = jiankangma.filename.split('.')[-1]
        hesuanjiance = form.hesuanjiance.data
        nhesuanjiance = hesuanjiance.filename.split('.')[-1]
        yimiaojiezhong = form.yimiaojiezhong.data
        nyimiaojiezhong = yimiaojiezhong.filename.split('.')[-1]
        jiaotonggongju = form.jiaotonggongju.data
        njiaotonggongju = jiaotonggongju.filename.split('.')[-1]
        foldername = name + "-" + numID
        nowPATH = os.path.join(UPLOAD_PATH, foldername)

        if os.path.exists(nowPATH):
            shutil.rmtree(nowPATH)
        os.makedirs(nowPATH)  # makedirs 创建文件时如果路径不存在会创建这个路径


        xingchengma.save(os.path.join(nowPATH, name + "-行程码." + nxingchengma))
        jiankangma.save(os.path.join(nowPATH, name + "-健康码." + njiankangma))
        hesuanjiance.save(os.path.join(nowPATH, name + "-核酸检测报告." + nhesuanjiance))
        yimiaojiezhong.save(os.path.join(nowPATH, name + "-疫苗接种记录." + nyimiaojiezhong))
        jiaotonggongju.save(os.path.join(nowPATH, name + "-乘坐交通工具始发及经停站点信息." + njiaotonggongju))
        return (u'提交成功')
    return render_template('upload.html', form=form)



# 访问上传的文件
# 浏览器访问：http://127.0.0.1:5000/images/django.jpg/  就可以查看文件了
@app.route('/333', methods=['GET', 'POST'])
def get_file():
    # print('1111')
    # start_dir = UPLOAD_PATH  # 要压缩的文件夹路径
    print(UPLOAD_PATH)
    file_news = '软件学院21级研究生.zip'  # 压缩后文件夹的名字
    print(file_news)
    if os.path.exists(os.path.join(os.path.dirname(__file__), file_news)):
        os.remove(os.path.join(os.path.dirname(__file__), file_news))
    z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)
    # print('22222')
    for dir_path, dir_names, file_names in os.walk(UPLOAD_PATH):
        f_path = dir_path.replace(UPLOAD_PATH, '')  # 这一句很重要，不replace的话，就从根目录开始复制
        f_path = f_path and f_path + os.sep or ''  # 实现当前文件夹以及包含的所有文件的压缩
        for filename in file_names:
            z.write(os.path.join(dir_path, filename), f_path + filename)
    z.close()
    # print(start_dir)
    # print(file_news)
    # send_from_directory(os.path.dirname(__file__),filename=file_news)
    directory = os.getcwd()  # 假设在当前目录
    response = make_response(send_from_directory(directory, file_news, as_attachment=True))
    response.headers["Content-Disposition"] = "attachment; filename={}".format(file_news.encode().decode('latin-1'))
    return response

    # return '下载中'







if __name__ == '__main__':
    app.run(Debug=True)
