import yaml
yaml.warnings({'YAMLLoadWarning': False})
import logging
import os
import sys

此處 = os.path.dirname(os.path.abspath(__file__))

class 假面:
    配置 = {}

    def 加載配置(self, 工程路徑):
        工程路徑 = os.path.relpath(工程路徑).replace('\\', '/')
        配置文件路徑 = f'{工程路徑}/工程配置.yaml'
        with open(配置文件路徑, encoding='utf8') as f:
            a = yaml.load(f)
            for i in a:
                self.配置.update(a[i])
        self.配置['工程路徑'] = 工程路徑
        self.配置['psd立繪路徑'] = os.path.join(工程路徑, self.配置['立繪文件夾'])
        self.配置['臨時立繪路徑'] = f"./{工程路徑}/_臨時立繪"
        self.配置['臨時立繪相對網頁路徑'] = os.path.relpath(self.配置['臨時立繪路徑'], f'{此處}/../html' ).replace('\\', '/')

    def __getattr__(self, x):
        return self.配置[x]


sys.modules[__name__] = 假面()
