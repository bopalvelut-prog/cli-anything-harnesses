import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('inform running')
@cli.command()
def start(): click.echo('inform started')
if __name__ == '__main__': cli()
