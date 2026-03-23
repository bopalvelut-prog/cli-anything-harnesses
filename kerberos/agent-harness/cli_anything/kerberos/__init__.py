import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('kerberos running')
@cli.command()
def start(): click.echo('kerberos started')
if __name__ == '__main__': cli()
