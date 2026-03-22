import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): subprocess.run(['odoo'])
@cli.command()
def modules(): click.echo('Odoo modules')
if __name__ == '__main__': cli()
