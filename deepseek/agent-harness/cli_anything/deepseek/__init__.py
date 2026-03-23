import click
@click.group()
def cli(): pass
@cli.command()
def chat(): click.echo('DeepSeek chat')
@cli.command()
def models(): click.echo('DeepSeek models')
if __name__ == '__main__': cli()
