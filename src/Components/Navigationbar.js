import React from "react";
import { Navbar, Nav, NavDropdown, Container } from 'react-bootstrap'

class Navigationbar extends React.Component {
    render() {
        return (
            <Navbar bg="light" expand="lg" sticky="top">
                <Container>
                    <Navbar.Brand href="#home">Cloud+</Navbar.Brand>
                    <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav">
                        <Nav className="me-auto">
                            <Nav.Link href="#home">Home</Nav.Link>
                            <NavDropdown title="Cloud Platforms" id="basic-nav-dropdown">
                                <NavDropdown.Item href="#cloud/3.1">Microsoft Azure</NavDropdown.Item>
                                <NavDropdown.Item href="#cloud/3.2">Amazon Web Services</NavDropdown.Item>
                                <NavDropdown.Item href="#cloud/3.3">Google Cloud Platform</NavDropdown.Item>
                                <NavDropdown.Divider />
                                <NavDropdown.Item href="#cloud/3.4">Other</NavDropdown.Item>
                            </NavDropdown>
                            <NavDropdown title="Services" id="basic-nav-dropdown">
                                <NavDropdown.Item href="#services/3.1">SAAS</NavDropdown.Item>
                                <NavDropdown.Item href="#services/3.2">PAAS</NavDropdown.Item>
                                <NavDropdown.Item href="#services/3.3">IAAS</NavDropdown.Item>
                                {/* lol can insert fontawesome icon here */}
                            </NavDropdown>
                        </Nav>
                        <Nav>
                        <Nav.Link href="#LoginPage">Login</Nav.Link>
                        </Nav>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
        )
    }
}
export default Navigationbar
