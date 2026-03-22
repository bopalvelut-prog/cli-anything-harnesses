import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('domain')
def find(domain): subprocess.run(['subfinder', '-d', domain])
@cli.command()
@click.argument('domain')
def passive(domain): subprocess.run(['subfinder', '-d', domain, '-passive'])
if __name__ == '__main__': cli()
