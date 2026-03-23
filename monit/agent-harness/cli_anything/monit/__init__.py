import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('monit running')
@cli.command()
def start(): click.echo('monit started')
if __name__ == '__main__': cli()
