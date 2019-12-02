///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Jun 12 2018)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

MyFrame1::MyFrame1( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	
	wxBoxSizer* bSizer2;
	bSizer2 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText1 = new wxStaticText( this, wxID_ANY, wxT("Welcome to e-Rubric system!"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText1->Wrap( -1 );
	
	m_staticText1->SetFont( wxFont( 16, wxFONTFAMILY_SWISS, wxFONTSTYLE_NORMAL, wxFONTWEIGHT_NORMAL, false, wxT("Sans") ) );
	m_staticText1->SetForegroundColour( wxSystemSettings::GetColour( wxSYS_COLOUR_HIGHLIGHT ) );
	
	bSizer2->Add( m_staticText1, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	
	bSizer2->Add( 0, 50, 0, wxALIGN_CENTER_HORIZONTAL, 5 );
	
	m_button1 = new wxButton( this, wxID_ANY, wxT("New Rubric"), wxDefaultPosition, wxDefaultSize, 0 );
	m_button1->SetDefault();
	
	bSizer2->Add( m_button1, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	m_button2 = new wxButton( this, wxID_ANY, wxT("Review Rubric"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer2->Add( m_button2, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	m_button3 = new wxButton( this, wxID_ANY, wxT("About"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer2->Add( m_button3, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	
	this->SetSizer( bSizer2 );
	this->Layout();
	
	this->Centre( wxBOTH );
	
	// Connect Events
	this->Connect( wxEVT_ACTIVATE, wxActivateEventHandler( MyFrame1::True ) );
}

MyFrame1::~MyFrame1()
{
	// Disconnect Events
	this->Disconnect( wxEVT_ACTIVATE, wxActivateEventHandler( MyFrame1::True ) );
	
}
