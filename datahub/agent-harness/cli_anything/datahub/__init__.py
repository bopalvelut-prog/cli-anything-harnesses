import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('datahub running')
@cli.command()
def start(): click.echo('datahub started')
if __name__ == '__main__': cli()
