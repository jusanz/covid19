<template>
  <div class="MainPage">
    <div class="Header mb-3">
      <page-header :icon="headerItem.icon">
        {{ headerItem.title }}
      </page-header>
      <div class="UpdatedAt">
        <span>{{ $t('最終更新') }} </span>
        <time :datetime="data.summary_updated_at">{{
          data.summary_updated_at
        }}</time>
      </div>
      <div v-if="!['ja', 'ja-basic'].includes($i18n.locale)" class="Annotation">
        <span>{{ $t('注釈') }} </span>
      </div>
    </div>
    <v-row class="DataBlock">
      <confirmed-cases-details-card
        :data="data.summary_data"
        :updated-at="data.summary_updated_at"
      />
      <confirmed-cases-attributes-card
        :data="data.patients_data"
        :updated-at="data.patients_updated_at"
        :sum-info="data.patients_sum"
      />
      <confirmed-cases-number-card
        :data="data.positives_data"
        :updated-at="data.tests_updated_at"
      />
      <inspection-persons-number-card
        :data="data.tests_data"
        :updated-at="data.tests_updated_at"
      />
      <tested-number-card
        :data="data.specimens_data"
        :updated-at="data.tests_updated_at"
      />
      <telephone-advisory-reports-number-card
        :data="data.helpline_data"
        :updated-at="data.helpline_updated_at"
      />
    </v-row>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { MetaInfo } from 'vue-meta'
import PageHeader from '@/components/PageHeader.vue'
import News from '@/data/news.json'
import ConfirmedCasesDetailsCard from '@/components/cards/ConfirmedCasesDetailsCard.vue'
import ConfirmedCasesNumberCard from '@/components/cards/ConfirmedCasesNumberCard.vue'
import ConfirmedCasesAttributesCard from '@/components/cards/ConfirmedCasesAttributesCard.vue'
import TestedNumberCard from '@/components/cards/TestedNumberCard.vue'
import InspectionPersonsNumberCard from '@/components/cards/InspectionPersonsNumberCard.vue'
import TelephoneAdvisoryReportsNumberCard from '@/components/cards/TelephoneAdvisoryReportsNumberCard.vue'

export default Vue.extend({
  components: {
    PageHeader,
    ConfirmedCasesDetailsCard,
    ConfirmedCasesNumberCard,
    ConfirmedCasesAttributesCard,
    TestedNumberCard,
    InspectionPersonsNumberCard,
    TelephoneAdvisoryReportsNumberCard
  },
  async asyncData({ $axios }) {
    const data = await $axios.$get('https://api.code4kochi.com/data/')
    return { data }
  },
  data() {
    const data = {
      headerItem: {
        icon: 'mdi-chart-timeline-variant',
        title: this.$t('高知県内の感染動向')
      },
      newsItems: News.newsItems
    }
    return data
  },
  head(): MetaInfo {
    return {
      title: this.$t('高知県内の感染動向') as string
    }
  }
})
</script>

<style lang="scss" scoped>
.MainPage {
  .Header {
    display: flex;
    flex-wrap: wrap;
    align-items: flex-end;

    @include lessThan($small) {
      flex-direction: column;
      align-items: baseline;
    }
  }

  .UpdatedAt {
    @include font-size(14);

    color: $gray-3;
    margin-bottom: 0.2rem;
  }

  .Annotation {
    @include font-size(12);

    color: $gray-3;
    @include largerThan($small) {
      margin: 0 0 0 auto;
    }
  }
  .DataBlock {
    margin: 20px -8px;

    .DataCard {
      @include largerThan($medium) {
        padding: 10px;
      }

      @include lessThan($small) {
        padding: 4px 8px;
      }
    }
  }
}
</style>
