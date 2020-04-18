// 全局的一些配置
export default {
  rootPath: '/product', // 发布到服务器的根目录，需以/开头但不能有尾/，如果只有/，请填写空字符串
  port: 8080, // 本地开发服务器的启动端口
  domain: 'dubbo.apache.org', // 站点部署域名，无需协议和path等
  defaultSearch: 'google', // 默认搜索引擎，baidu或者google
  defaultLanguage: 'en-us',
  'en-us': {
    pageMenu: [
      {
        key: 'home', // 用作顶部菜单的选中
        text: 'Home',
        link: '/en-us/index.html',
      },
      {
        key: 'docs',
        text: 'Resources',
        link: '/en-us/docs/isle.html',
      },
      {
        key: 'blog',
        text: 'Work',
        link: '/en-us/blog/index.html',
      },
      {
        key: 'community',
        text: 'Community',
        link: '/en-us/community/index.html',
      },
    ],
    disclaimer: {
      title: 'Disclaimer',
      content: 'the disclaimer content',
    },
    documentation: {
      title: 'Resources',
      list: [
        {
          text: 'Overview',
          link: '/en-us/docs/isle.html',
        },
        {
          text: 'Comprehensive research',
          link: '/en-us/docs/compre.html',
        },
        {
          text: 'Journal',
          link: '/en-us/docs/dir/journal.html',
        },
      ],
    },
    resources: {
      title: 'Work and communication',
      list: [
        {
          text: 'Blog',
          link: '/en-us/blog/index.html',
        },
        {
          text: 'Community',
          link: '/en-us/community/index.html',
        },
      ],
    },
    copyright: 'Copyright © 2020 Shaoqing Dai',
  },
  'zh-cn': {
    pageMenu: [
      {
        key: 'home',
        text: '首页',
        link: '/zh-cn/index.html',
      },
      {
        key: 'docs',
        text: '资源列表',
        link: '/zh-cn/docs/isle.html',
      },
      {
        key: 'blog',
        text: '研究工作',
        link: '/zh-cn/blog/index.html',
      },
      {
        key: 'community',
        text: '社区',
        link: '/zh-cn/community/index.html',
      },
    ],
    disclaimer: {
      title: '免责声明',
      content: '免责声明的具体内容',
    },
    documentation: {
      title: '资源列表',
      list: [
        {
          text: '概览',
          link: '/zh-cn/docs/isle.html',
        },
        {
          text: '综合性研究',
          link: '/zh-cn/docs/compre.html',
        },
        {
          text: '期刊资源',
          link: '/zh-cn/docs/dir/journal.html',
        },
      ],
    },
    resources: {
      title: '研究工作与交流',
      list: [
        {
          text: '研究工作',
          link: '/zh-cn/blog/index.html',
        },
        {
          text: '社区',
          link: '/zh-cn/community/index.html',
        },
      ],
    },
    copyright: 'Copyright © 2020 戴劭勍',
  },
};
