<template>
  <form>
    <md-card>
      <md-card-header :data-background-color="dataBackgroundColor">
        <h4 class="title">Edit Company Profile</h4>
        <p class="category">Complete your profile</p>
      </md-card-header>

      <md-card-content>
        <div class="md-layout">
          <div class="md-layout-item md-small-size-100 md-size-100">
            <md-field>
              <label>Company Name</label>
              <md-input v-model="info.companyName" type="text"></md-input>
            </md-field>
          </div>
          <div class="md-layout-item md-small-size-100 md-size-33">
            <md-field>
              <label>Annual Revenue</label>
              <md-input v-model="info.annualRevenue" type="number"></md-input>
            </md-field>
          </div>
          <div class="md-layout-item md-small-size-100 md-size-33">
            <md-field>
              <label>Yoy Growth rate</label>
              <md-input v-model="info.yoyGrowth" type="number"></md-input>
            </md-field>
          </div>
          <div class="md-layout-item md-small-size-100 md-size-33">
            <md-field>
              <label>Capital Seeking</label>
              <md-input v-model="info.capitalSeeking" type="number"></md-input>
            </md-field>
          </div>
          <div class="md-layout-item md-small-size-100 md-size-33">
            <md-field>
              <label>Monthly Burn</label>
              <md-input v-model="info.monthlyBurn" type="number"></md-input>
            </md-field>
          </div>
          <div class="md-layout-item md-small-size-100 md-size-33">
            <md-field>
              <label>Investment Term Length</label>
              <md-input v-model="info.investmentPeriod" type="number"></md-input>
            </md-field>
          </div>
          <div class="md-layout-item md-small-size-100 md-size-33">
            <md-field>
              <label>Outstanding Shares</label>
              <md-input v-model="info.outstandingShares" type="number"></md-input>
            </md-field>
          </div>
          <div class="md-layout-item md-small-size-100 md-size-33">
            <md-field>
              <label>Capital Cost (Optional)</label>
              <md-input type="number"></md-input>
            </md-field>
          </div>
          <div class="md-layout-item md-small-size-100 md-size-33">
            <md-field>
              <label>Standard Industry Multiplier</label>
              <md-input v-model="info.industryMultiplier" type="number"></md-input>
            </md-field>
          </div>
          <div class="md-layout-item md-small-size-100 md-size-33">
            <md-field>
                <label>EBIDTA (Optional)</label>
                <md-input  type="number"></md-input>
            </md-field>
          </div>
          <div class="md-layout-item md-small-size-100 md-size-33">
            <md-field>
                <label>Free cash flow (Optional)</label>
                <md-input  type="number"></md-input>
            </md-field>
          </div>
          <div class="md-layout-item md-small-size-100 md-size-33">
            <md-field>
                <label>Sales: Annual (Optional)</label>
                <md-input  type="number"></md-input>
            </md-field>
          </div>
          <div class="md-layout-item md-small-size-100 md-size-33">
            <md-field>
                <label>Sales: Monthly (Optional)</label>
                <md-input  type="number"></md-input>
            </md-field>
          </div>
          <div class="md-layout-item md-small-size-100 md-size-33">
            <md-field>
                <label>Cost Per Acquisition (Optional)</label>
                <md-input  type="number"></md-input>
            </md-field>
          </div>
          <div class="md-layout-item md-small-size-100 md-size-33">
            <md-field>
                <label>Return On Advertising Spending (Optional)</label>
                <md-input  type="number"></md-input>
            </md-field>
          </div>
          <div class="md-layout-item md-small-size-100 md-size-33">
            <md-field>
                <label>Revenue Run Rate (Optional)</label>
                <md-input  type="number"></md-input>
            </md-field>
          </div>
          <div class="md-layout-item md-small-size-100 md-size-33">
            <md-field>
                <label>Average LTV (Optional)</label>
                <md-input  type="number"></md-input>
            </md-field>
          </div>
          <div class="md-layout-item md-small-size-100 md-size-33">
            <md-field>
                <label>ARPU (Optional)</label>
                <md-input  type="number"></md-input>
            </md-field>
          </div>
          <div class="md-layout-item md-small-size-100 md-size-33">
            <md-field>
                <label>Churn Rate (Optional)</label>
                <md-input  type="number"></md-input>
            </md-field>
          </div>
          <div class="md-layout-item md-small-size-100 md-size-100">
            <md-field>
              <label>Industry Vertical</label>
              <md-input v-model="info.industryVertical" type="text"></md-input>
            </md-field>
          </div>
          <div class="md-layout-item md-size-100 text-right">
            <md-button  class="md-raised md-success" @click="updateMetrics">Update Profile</md-button>
          </div>
        </div>
      </md-card-content>
    </md-card>
  </form>
</template>
<script>
export default {
  name: "edit-profile-form",
  props: {
    dataBackgroundColor: {
      type: String,
      default: ""
    }
  },
  data() {
    return {
        returnvalue: null,
        info: {
            companyName: "", //: username, null,
            annualRevenue: "",
            yoyGrowth: "",
            capitalSeeking: "",
            monthlyBurn: "",
            investmentPeriod: "",
            outstandingShares: "",
            industryVertical: "",
            industryMultiplier: ""
        },
        errors: []

      /*disabled: null,
      emailadress: null,
      lastname: null,
      firstname: null,
      address: null,
      city: null,
      country: null,
      code: null,
      aboutme:
        ""*/
    };
  }, methods: {
      updateMetrics(){
          //let newMetric = this.metricUpdate;


          /*let newMetric = {
              companyName: this.metricUpdate.companyName,
              annualRevenue: this.metricUpdate.annualRevenue,
              yoyGrowth: this.metricUpdate.yoyGrowth,
              capitalSeeking: this.metricUpdate.capitalSeeking,
              monthlyBurn: this.metricUpdate.monthlyBurn,
              investmentPeriod: this.metricUpdate.investmentPeriod,
              industryMultiplier: 3, //this.metricUpdate.industryMultiplier,
              outstandingShares: this.metricUpdate.outstandingShares,
              industyVertical: this.metricUpdate.industryVertical
          }*/

          
          let newMetric = {
              companyName: this.info.companyName,
              annualRevenue: this.info.annualRevenue,
              yoyGrowth: this.info.yoyGrowth,
              capitalSeeking: this.info.capitalSeeking,
              monthlyBurn: this.info.monthlyBurn,
              investmentPeriod: this.info.investmentPeriod,
              industryMultiplier: 3, //this.metricUpdate.industryMultiplier,
              outstandingShares: this.info.outstandingShares,
              industyVertical: this.info.industryVertical
          }

          console.log(newMetric);

          this.$http.put(`https://investors.opn.ninja:8081/api/valuationMetrics/${this.$store.state.user.pk}/`, newMetric)
          .then(response => {
              this.returnvalue = response.data;
              console.log("put")
              return
              console.log('after')
          })
          .catch(function(error) {
              console.log(error.request);
              console.log("error")
          })

          this.$http.post(`https://investors.opn.ninja:8081/api/valuationMetrics/${this.$store.state.user.pk}/`, newMetric)
          .then(response => {
              this.returnvalue= response.data;
              console.log("post")
              return
              console.log("post_after")
          })
          .catch(function(error) {
              console.log(error.request);
              console.log("post_error")
          })

          /*this.metricUpdate.companyName = "";
          this.metricUpdate.annualRevenue = "";
          this.metricUpdate.yoyGrowth = "";
          this.metricUpdate.capitalSeeking = "";
          this.metricUpdate.monthlyBurn = "";
          this.metricUpdate.investmentPeriod = "";
          this.metricUpdate.industryMultiplier = "";
          this.metricUpdate.outstandingShares = "";
          this.metricUpdate.industryVertical = "";*/

      }

  },

  created() {
      this.$http.get(`https://investors.opn.ninja:8081/api/valuationMetrics/${this.$store.state.user.pk}/`)
      .then(response => {
          this.info = response.data;
          console.log(response);
      })
      .catch(err => {
      this.errors.push(err)})
  }
};


</script>
<style></style>
