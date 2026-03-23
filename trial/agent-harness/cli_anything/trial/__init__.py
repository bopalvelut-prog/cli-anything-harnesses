import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('trial running')
@cli.command()
def start(): click.echo('trial started')
if __name__ == '__main__': cli()
