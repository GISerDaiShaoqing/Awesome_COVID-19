import React from 'react';

export default {
  'zh-cn': {
    brand: {
      brandName: 'COVID-19研究资源',
      briefIntroduction: '关于COVID-19的各项研究资源集锦的网站',
      buttons: [
        {
          text: '立即开始',
          link: '/zh-cn/docs/isle.html',
          type: 'primary',
        },
        {
          text: '查看Github',
          link: 'https://github.com/GISerDaiShaoqing/Awesome_COVID-19',
          type: 'normal',
        },
      ],
    },
    introduction: {
      title: 'COVID-19疫情发展概览',
      desc: 'COVID-19疫情时间序列变化趋势，数据源: https://github.com/ExpDev07/coronavirus-tracker-api; https://github.com/CSSEGISandData/COVID-19; https://github.com/mathdroid/covid-19-api。',
      img: '/img/architecture.png',
    },
    features: {
      title: '研究主题',
      list: [
        {
          //img: '/img/feature_transpart.png',
          img: '/img/ISLElogo.jpg',
          title: '空间生命历程流行病学',
          content: '',
        },
        {
          //img: '/img/feature_loadbalances.png',
          img: '/img/gis.png',
          title: '地理信息系统',
          content: '',
        },
        {
          //img: '/img/feature_service.png',
          img: '/img/RSEO.png',
          title: '卫星遥感',
          content: '',
        },
        {
          //img: '/img/feature_hogh.png',
          img: '/img/sensor.png',
          title: '全球定位与传感器',
          content: '',
        },
        {
          //img: '/img/feature_runtime.png',
          img: '/img/statistics.png',
          title: '统计学',
          content: '',
        },
        {
          //img: '/img/feature_maintenance.png',
          img: '/img/machinelearning.png',
          title: '机器学习',
          content: '',
        },
      ],
    },
    start: {
      title: 'COVID-19 Shiny app',
      desc: 'COVID-19疫情仪表盘',
      img: '/img/quick_start.png',
      button: {
        text: '阅读更多',
        link: '/zh-cn/docs/isle.html',
      },
    },
    users: {
      title: '贡献者',
      desc: <span></span>,
      list: [
        //'/img/users_alibaba.png',
        '/img/card.jpg',
      ],
    },
  },
  'en-us': {
    brand: {
      brandName: 'Awesome COVID-19',
      briefIntroduction: 'Resources of COVID-19 research',
      buttons: [
        {
          text: 'Quick Start',
          link: '/en-us/docs/isle.html',
          type: 'primary',
        },
        {
          text: 'View on Github',
          link: 'https://github.com/GISerDaiShaoqing/Awesome_COVID-19',
          type: 'normal',
        },
      ],
    },
    introduction: {
      title: 'Overview of COVID-19',
      desc: 'Timeseries data of COVID-19, data sources: https://github.com/ExpDev07/coronavirus-tracker-api; https://github.com/CSSEGISandData/COVID-19; https://github.com/mathdroid/covid-19-api.',
      img: '/img/architecture.png',
    },
    features: {
      title: 'Topics',
      list: [
        {
          //img: '/img/feature_transpart.png',
          img: '/img/ISLElogo.jpg',
          title: 'Spatial Lifecourse Epidemiology',
          content: '',
        },
        {
          //img: '/img/feature_loadbalances.png',
          img: '/img/gis.png',
          title: 'GIS',
          content: '',
        },
        {
          //img: '/img/feature_service.png',
          img: '/img/RSEO.png',
          title: 'Satellite and Remote Sensing',
          content: '',
        },
        {
          //img: '/img/feature_hogh.png',
          img: '/img/sensor.png',
          title: 'GPS and Sensors',
          content: '',
        },
        {
          //img: '/img/feature_runtime.png',
          img: '/img/statistics.png',
          title: 'Statistics',
          content: '',
        },
        {
          //img: '/img/feature_maintenance.png',
          img: '/img/machinelearning.png',
          title: 'Machine Learning',
          content: '',
        }
      ]
    },
    start: {
      title: 'COVID-19 Shiny app',
      desc: 'The dashboard of COVID-19',
      img: '/img/quick_start.png',
      button: {
        text: 'READ MORE',
        link: '/en-us/docs/isle.html',
      },
    },
    users: {
      title: 'Contributors',
      desc: <span></span>,
      list: [
        //'/img/users_alibaba.png',
        '/img/card.jpg',
      ],
    },
  },
};
