import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bind running')
@cli.command()
def start(): click.echo('bind started')
if __name__ == '__main__': cli()
