<template>
  <v-col cols="12" md="6" class="DataCard">
    <time-bar-chart
      :title="$t('新型コロナ健康相談センター相談件数')"
      :title-id="'number-of-reports-to-covid19-telephone-advisory-center'"
      :chart-id="'time-bar-chart-contacts'"
      :chart-data="data"
      :date="updatedAt"
      :unit="$t('件.reports')"
      :url="'https://catalog.data.metro.tokyo.lg.jp/dataset/t000010d0000000071'"
    />
    <!-- 件.reports = 窓口相談件数 -->
  </v-col>
</template>

<script>
import Data from '@/data/data.json'
import formatGraph from '@/utils/formatGraph'
import TimeBarChart from '@/components/TimeBarChart.vue'

export default {
  components: {
    TimeBarChart
  },
  props: {
    data: {
      type: Array,
      default: () => {}
    },
    updatedAt: {
      type: String,
      default: ''
    }
  },
  data() {
    // 相談件数
    const contactsGraph = formatGraph(Data.contacts.data)

    const data = {
      Data,
      contactsGraph
    }
    return data
  }
}
</script>
