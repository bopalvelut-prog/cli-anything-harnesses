import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('junior running')
@cli.command()
def start(): click.echo('junior started')
if __name__ == '__main__': cli()
