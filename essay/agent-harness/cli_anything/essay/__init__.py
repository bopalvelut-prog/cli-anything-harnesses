import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('essay running')
@cli.command()
def start(): click.echo('essay started')
if __name__ == '__main__': cli()
