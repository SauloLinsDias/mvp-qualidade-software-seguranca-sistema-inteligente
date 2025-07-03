import {
  Box,
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Typography,
} from '@mui/material'

type TablePatientsProps = {
  patients: Array<Patient>
}

const TablePatients = (props: TablePatientsProps) => {
  const { patients } = props

  const objectModified = {
    st_slope: {
      Up: 'Inclinação Ascendente',
      Flat: 'Inclinação Plana',
      Down: 'Inclinação Descendente',
    },
    chest_pain_type: {
      TA: 'Angina Típica',
      ATA: 'Angina Atípica',
      NAP: 'Dor Não Anginosa',
      ASY: 'Assintomática',
    },
    resting_ecg: {
      Normal: 'Normal',
      ST: 'Anormalidade ST-T',
      LVH: 'Hipertrofia Ventricular Esquerda',
    },
  }

  return (
    <Box>
      <Box sx={{ textAlign: 'center', mb: 4, mt: 2 }}>
        <Typography variant="h2" sx={{ mb: 2 }}>
          Tabela de Pacientes
        </Typography>
        <Typography>
          Visualize os dados dos pacientes registrados e suas análises de risco.
        </Typography>
      </Box>
      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Nome</TableCell>
              <TableCell>Idade</TableCell>
              <TableCell>Gênero</TableCell>
              <TableCell>Tipo de Dor no Peito</TableCell>
              <TableCell>Pressão Arterial (mm Hg)</TableCell>
              <TableCell>Colesterol (mg/dl)</TableCell>
              <TableCell>Glicose em jejum (mg/dl)</TableCell>
              <TableCell>Eletrocardiograma</TableCell>
              <TableCell>Frequência Cardíaca Máxima</TableCell>
              <TableCell>Angina Induzida por Exercício</TableCell>
              <TableCell>Depressão Induzida por Exercício</TableCell>
              <TableCell>Inclinação do Segmento ST</TableCell>
              <TableCell>Resultado</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {patients
              .sort((a, b) => b.id - a.id)
              .map((patient) => (
                <TableRow key={patient.id}>
                  <TableCell>{patient.name}</TableCell>
                  <TableCell>{patient.age}</TableCell>
                  <TableCell>{patient.sex}</TableCell>
                  <TableCell>
                    {objectModified['chest_pain_type'][patient.chest_pain_type]}
                  </TableCell>
                  <TableCell>{patient.resting_bp}</TableCell>
                  <TableCell>{patient.cholesterol}</TableCell>
                  <TableCell>{patient.fasting_bs}</TableCell>
                  <TableCell>{objectModified['resting_ecg'][patient.resting_ecg]}</TableCell>
                  <TableCell>{patient.max_hr}</TableCell>
                  <TableCell>{patient.exercise_angina ? 'Sim' : 'Não'}</TableCell>
                  <TableCell>{patient.oldpeak}</TableCell>
                  <TableCell>{objectModified['st_slope'][patient.st_slope]}</TableCell>
                  <TableCell>
                    {patient.heart_disease === 1 ? 'Doença Cardíaca' : 'Saudável'}
                  </TableCell>
                </TableRow>
              ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Box>
  )
}

export default TablePatients
