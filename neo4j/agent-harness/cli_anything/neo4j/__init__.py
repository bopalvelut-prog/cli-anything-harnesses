import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): subprocess.run(['neo4j', 'start'])
@cli.command()
def stop(): subprocess.run(['neo4j', 'stop'])
@cli.command()
def status(): subprocess.run(['neo4j', 'status'])
@cli.command()
def cypher(): subprocess.run(['cypher-shell', 'RETURN 1'])
if __name__ == '__main__': cli()
