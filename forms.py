# -*- coding: utf-8 -*-
# coding=utf-8
from flask_wtf import FlaskForm
from wtforms import Form, FileField, StringField, SubmitField
from wtforms.validators import InputRequired
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
    yimiaojiezhong = FileField(u'疫苗接种凭证',validators=[FileRequired(),  # FileRequired必须上传
                                           FileAllowed(['jpg', 'png', 'jpeg'])  # FileAllowed:必须为指定的格式的文件
                                           ])
    jiaotonggongju = FileField(u'乘坐交通工具始发及经停站点信息',validators=[FileRequired(),  # FileRequired必须上传
                                           FileAllowed(['jpg', 'png', 'jpeg'])  # FileAllowed:必须为指定的格式的文件
                                           ])
    submit = SubmitField(u'添加')