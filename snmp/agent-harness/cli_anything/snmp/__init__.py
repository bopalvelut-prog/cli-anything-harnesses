import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('snmp running')
@cli.command()
def start(): click.echo('snmp started')
if __name__ == '__main__': cli()
