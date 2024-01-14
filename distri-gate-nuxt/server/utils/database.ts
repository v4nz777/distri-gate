import postgres from "postgres"


export const pgConnection = ():postgres.Sql => {
    
    return postgres({
        database:process.env.PGDATABASE,
        host: process.env.PGHOST,
        username: process.env.PGUSER,
        password: process.env.PGPASSWORD,
        ssl: 'require',
        port: 5432,
    })
}