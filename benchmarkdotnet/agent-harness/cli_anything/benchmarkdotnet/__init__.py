import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('benchmarkdotnet running')
@cli.command()
def start(): click.echo('benchmarkdotnet started')
if __name__ == '__main__': cli()
