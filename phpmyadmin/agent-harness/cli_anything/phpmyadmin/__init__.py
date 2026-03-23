import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('phpmyadmin running')
@cli.command()
def start(): click.echo('phpmyadmin started')
if __name__ == '__main__': cli()
