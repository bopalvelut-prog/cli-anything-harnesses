import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bind9 running')
@cli.command()
def start(): click.echo('bind9 started')
if __name__ == '__main__': cli()
