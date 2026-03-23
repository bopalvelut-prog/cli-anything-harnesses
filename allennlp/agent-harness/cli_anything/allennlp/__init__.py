import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('allennlp running')
@cli.command()
def start(): click.echo('allennlp started')
if __name__ == '__main__': cli()
