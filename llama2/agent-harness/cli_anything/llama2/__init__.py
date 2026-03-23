import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('llama2 running')
@cli.command()
def start(): click.echo('llama2 started')
if __name__ == '__main__': cli()
