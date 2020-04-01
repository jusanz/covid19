<template>
  <v-col cols="12" md="6" class="DataCard">
    <data-table
      :title="$t('陽性患者の属性')"
      :title-id="'attributes-of-confirmed-cases'"
      :chart-data="data"
      :chart-option="{}"
      :date="updatedAt"
      :info="sumInfo"
      :url="'https://catalog.data.metro.tokyo.lg.jp/dataset/t000010d0000000068'"
      :source="$t('オープンデータを入手')"
    />
  </v-col>
</template>

<script>
import DataTable from '@/components/DataTable.vue'

export default {
  components: {
    DataTable
  },
  props: {
    data: {
      type: Array,
      default: () => {}
    },
    updatedAt: {
      type: String,
      default: ''
    },
    sumInfo: {
      type: Object,
      default: () => {}
    }
  }
}
</script>
