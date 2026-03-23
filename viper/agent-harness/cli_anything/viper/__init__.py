import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('viper running')
@cli.command()
def start(): click.echo('viper started')
if __name__ == '__main__': cli()
