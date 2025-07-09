import {
  Box,
  Button,
  FormControl,
  FormHelperText,
  Grid,
  InputLabel,
  MenuItem,
  Select,
  TextField,
  Typography,
} from '@mui/material'
import axios from 'axios'
import Swal from 'sweetalert2'

type PatientFormProps = {
  onSubmit?: (data: Record<string, string | number>) => void
}

const PatientForm = (props: PatientFormProps) => {
  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    try {
      event.preventDefault()
      const formData = new FormData(event.currentTarget)
      const data = Object.fromEntries(formData.entries())

      const { data: response } = await axios.post('http://localhost:5000/patients/', data)
      const { heart_disease } = response

      if (props?.onSubmit) {
        props.onSubmit(data as Record<string, string | number>)
      }

      if (heart_disease) {
        Swal.fire({
          title: 'Alerta de Saúde',
          text: 'O paciente apresenta risco de doenças cardíacas.',
          icon: 'warning',
          confirmButtonText: 'OK',
        })
      } else {
        Swal.fire({
          title: 'Saúde Estável',
          text: 'O paciente não apresenta risco de doenças cardíacas.',
          icon: 'success',
          confirmButtonText: 'OK',
        })
      }
    } catch (error) {
      console.error('Erro ao enviar os dados do paciente:', error)
      Swal.fire({
        title: 'Erro',
        text: 'Ocorreu um erro ao enviar os dados do paciente. Por favor, tente novamente.',
        icon: 'error',
        confirmButtonText: 'OK',
      })
    }
  }

  return (
    <Box component="form" sx={{ display: 'grid', gap: 3 }} onSubmit={handleSubmit}>
      <Typography variant="h4" component="h2" gutterBottom>
        Formulário de Paciente
      </Typography>
      <Typography variant="body1" gutterBottom>
        Preencha os dados do paciente abaixo para análise de risco de doenças cardíacas.
      </Typography>
      <Grid container columns={4} spacing={2}>
        <Grid size={1}>
          <TextField required label="Nome" name="name" fullWidth />
        </Grid>
        <Grid size={1}>
          <TextField
            required
            label="Idade"
            name="age"
            type="number"
            helperText="Idade do paciente (em anos)"
            fullWidth
          />
        </Grid>
        <Grid size={1}>
          <FormControl required fullWidth>
            <InputLabel>Sexo</InputLabel>
            <Select name="sex" defaultValue="">
              <MenuItem value="M">Masculino</MenuItem>
              <MenuItem value="F">Feminino</MenuItem>
            </Select>
            <FormHelperText>Sexo do paciente</FormHelperText>
          </FormControl>
        </Grid>
        <Grid size={1}>
          <FormControl required fullWidth>
            <InputLabel>Tipo de Dor no Peito</InputLabel>
            <Select name="chest_pain_type" defaultValue="">
              <MenuItem value="TA">Angina Típica</MenuItem>
              <MenuItem value="ATA">Angina Atípica</MenuItem>
              <MenuItem value="NAP">Dor Não Anginosa</MenuItem>
              <MenuItem value="ASY">Assintomática</MenuItem>
            </Select>
            <FormHelperText>Classificação da dor no peito</FormHelperText>
          </FormControl>
        </Grid>
        <Grid size={1}>
          <TextField
            required
            label="Pressão Arterial em Repouso"
            name="resting_bp"
            type="number"
            helperText="Pressão arterial sistólica em repouso (mm Hg)"
            fullWidth
          />
        </Grid>
        <Grid size={1}>
          <TextField
            required
            label="Colesterol"
            name="cholesterol"
            type="number"
            helperText="Colesterol sérico (mg/dl)"
            fullWidth
          />
        </Grid>
        <Grid size={1}>
          <TextField
            required
            label="Glicose em Jejum"
            name="fasting_bs"
            type="number"
            helperText="Glicose em jejum (mg/dl)"
            fullWidth
          />
        </Grid>
        <Grid size={1}>
          <FormControl required fullWidth>
            <InputLabel>Eletrocardiograma em Repouso</InputLabel>
            <Select name="resting_ecg" defaultValue="">
              <MenuItem value="Normal">Normal</MenuItem>
              <MenuItem value="ST">Anormalidade na onda ST-T</MenuItem>
              <MenuItem value="LVH">Hipertrofia Ventricular Esquerda</MenuItem>
            </Select>
            <FormHelperText>Resultado do eletrocardiograma em repouso</FormHelperText>
          </FormControl>
        </Grid>
        <Grid size={1}>
          <TextField
            required
            label="Frequência Cardíaca Máxima"
            name="max_hr"
            type="number"
            helperText="Valor entre 60 e 202 bpm"
            fullWidth
          />
        </Grid>
        <Grid size={1}>
          <FormControl required fullWidth>
            <InputLabel>Angina Induzida por Exercício</InputLabel>
            <Select name="exercise_angina" defaultValue="">
              <MenuItem value="1">Sim</MenuItem>
              <MenuItem value="0">Não</MenuItem>
            </Select>
            <FormHelperText>Presença de angina durante esforço físico</FormHelperText>
          </FormControl>
        </Grid>
        <Grid size={1}>
          <TextField
            required
            label="Oldpeak (Depressão do Segmento ST)"
            name="oldpeak"
            type="number"
            helperText="Valor numérico medido em depressão"
            fullWidth
          />
        </Grid>
        <Grid size={1}>
          <FormControl fullWidth required>
            <InputLabel>Inclinação do Segmento ST</InputLabel>
            <Select name="st_slope" defaultValue="">
              <MenuItem value="Up">Ascendente</MenuItem>
              <MenuItem value="Flat">Plana</MenuItem>
              <MenuItem value="Down">Descendente</MenuItem>
            </Select>
            <FormHelperText>Inclinação do segmento ST durante o esforço</FormHelperText>
          </FormControl>
        </Grid>
        <Grid offset={3} size={1}>
          <Button fullWidth variant="contained" type="submit">
            Enviar para análise
          </Button>
        </Grid>
      </Grid>
    </Box>
  )
}

export default PatientForm
