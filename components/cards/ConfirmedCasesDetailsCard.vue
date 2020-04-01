<template>
  <v-col cols="12" md="6" class="DataCard">
    <confirmed-cases-card
      :title="$t('検査陽性者の状況')"
      :title-id="'details-of-confirmed-cases'"
      :date="updatedAt"
    >
      <confirmed-cases-table
        :aria-label="$t('検査陽性者の状況')"
        v-bind="data"
      />
    </confirmed-cases-card>
  </v-col>
</template>

<script>
import ConfirmedCasesCard from '@/components/ConfirmedCasesCard.vue'
import ConfirmedCasesTable from '@/components/ConfirmedCasesTable.vue'

export default {
  components: {
    ConfirmedCasesCard,
    ConfirmedCasesTable
  },
  props: {
    data: {
      type: Object,
      default: () => {}
    },
    updatedAt: {
      type: String,
      default: ''
    }
  }
}
</script>
