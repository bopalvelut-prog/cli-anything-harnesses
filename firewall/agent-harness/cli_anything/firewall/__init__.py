import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('firewall running')
@cli.command()
def start(): click.echo('firewall started')
if __name__ == '__main__': cli()
