import MenuIcon from '@mui/icons-material/Menu'
import {
  AppBar,
  Box,
  Card,
  CardContent,
  Container,
  IconButton,
  Toolbar,
  Typography,
} from '@mui/material'
import axios from 'axios'
import { useEffect, useState } from 'react'
import Swal from 'sweetalert2'
import PatientForm from './components/PatientForm'
import TablePatients from './components/TablePatients'

function App() {
  const [patients, setPatients] = useState<Patient[]>([])

  const fetchPatients = async () => {
    try {
      const response = await axios.get<Patient[]>('http://localhost:5000/patients/')
      setPatients(response.data)

      return response.data
    } catch (error) {
      console.error('Erro ao buscar pacientes:', error)
      Swal.fire({
        title: 'Erro',
        text: 'Ocorreu um erro ao buscar os pacientes. Por favor, tente novamente.',
        icon: 'error',
        confirmButtonText: 'OK',
      })
      return []
    }
  }

  useEffect(() => {
    fetchPatients()
  }, [])

  return (
    <>
      <AppBar position="relative" sx={{ mb: 2, py: 2 }}>
        <Toolbar variant="dense">
          <IconButton edge="start" color="inherit" aria-label="menu" sx={{ mr: 2 }}>
            <MenuIcon />
          </IconButton>
          <Typography variant="h6" color="inherit" component="div">
            HeartApp
          </Typography>
        </Toolbar>
      </AppBar>
      <Container>
        <Box sx={{ textAlign: 'center', mb: 4, mt: 2 }}>
          <Typography variant="h2" sx={{ mb: 2 }}>
            Bem-vindo ao projeto de predição de doenças cardíacas!
          </Typography>
          <Typography>
            Este projeto utiliza técnicas de Machine Learning para prever a probabilidade de doenças
            cardíacas com base em dados clínicos.
          </Typography>
          <Typography>
            Explore os recursos e descubra como a inteligência artificial pode ajudar na detecção
            precoce de problemas cardíacos.
          </Typography>
        </Box>
        <Card elevation={1}>
          <CardContent>
            <PatientForm onSubmit={fetchPatients} />
          </CardContent>
        </Card>
        <Card elevation={1}>
          <CardContent>
            <TablePatients patients={patients} />
          </CardContent>
        </Card>
      </Container>
    </>
  )
}

export default App
