package dao;

import java.sql.Connection;
import java.util.ArrayList;

public class DAOTablaEventos {

	/**
	 * Arraylits de recursos que se usan para la ejecución de sentencias SQL
	 */
	private ArrayList<Object> recursos;

	/**
	 * Atributo que genera la conexión a la base de datos
	 */
	private Connection conn;

	/**
	 * Metodo constructor que crea DAOVideo
	 * <b>post: </b> Crea la instancia del DAO e inicializa el Arraylist de recursos
	 */

	public DAOTablaEventos(){
		recursos = new ArrayList<Object>();
	}
	
	
	
	
}
