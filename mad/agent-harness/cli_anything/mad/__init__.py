import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mad running')
@cli.command()
def start(): click.echo('mad started')
if __name__ == '__main__': cli()
