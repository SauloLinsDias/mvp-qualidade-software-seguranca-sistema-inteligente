type Patient = {
  id: number
  name: string
  age: number
  sex: string
  chest_pain_type: 'TA' | 'ATA' | 'NAP' | 'ASY'
  resting_bp: number
  cholesterol: number
  fasting_bs: number
  resting_ecg: 'Normal' | 'ST' | 'LVH'
  max_hr: number
  exercise_angina: boolean
  oldpeak: number
  st_slope: 'Up' | 'Flat' | 'Down'
  heart_disease: number
  created_at: string
}
