import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('metrics running')
@cli.command()
def start(): click.echo('metrics started')
if __name__ == '__main__': cli()
