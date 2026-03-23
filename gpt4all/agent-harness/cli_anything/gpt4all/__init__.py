import click
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('GPT4All start')
@cli.command()
def models(): click.echo('GPT4All models')
if __name__ == '__main__': cli()
